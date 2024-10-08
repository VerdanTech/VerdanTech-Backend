# Standard Library
import html
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Any

# External Libraries
import html2text

# VerdanTech Source
from src.common.adapters.utils import read_file_async
from src.common.interfaces.email import AbstractEmailClient


class BaseEmailClient(AbstractEmailClient):
    """
    Partial implemention of the AbstractAsyncEmailClient interface defined in interfaces.

    Contains implementation of html parsing and message compilation.

    The implementation of the "send" awaitable is the responsibility of subclasses.
    """

    def __init__(
        self,
        hostname: str,
        port: int,
        username: str,
        password: str,
        sender: str,
    ):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.sender = sender

    def template_html(self, html_content: str, **kwargs: dict[str, Any]) -> str:
        """
        Replace templated variables contained in {{}} with kwargs.

        Args:
            filepath (str): the path of the email html document.
            kwargs (dict[str, Any]): arguments to insert into html.

        Raises:
            ValueError: Raised if not all templated valued are
                filled by provided with kwargs.

        Returns:
            str: the html string.
        """

        # Find all templated values in html_content
        templated_vars = set(re.findall(r"{{\w+}}", html_content))

        # Remove the {{ and }} from each templated variable to get just the names
        templated_var_names = {var[2:-2] for var in templated_vars}

        # Check if all keys in kwargs match a templated variable name in html_content
        for key in kwargs.keys():
            if key not in templated_var_names:
                raise ValueError(
                    f"""
                    Error while constructing email: the argument {key} 
                    does not match any templated variable in the html content
                    """
                )

        # Replace templated values with kwargs
        for key, value in kwargs.items():
            html_content = html_content.replace(
                f"{{{{{key}}}}}", html.escape(str(value))
            )

        # Check if there are any un-replaced templated variables left
        leftover_vars = re.findall(r"{{\w+}}", html_content)
        if leftover_vars:
            leftover_vars = ", ".join(leftover_vars)
            raise ValueError(
                f"""Error while constructing email: 
                the following variables were not replaced: 
                {leftover_vars}
                """
            )

        return html_content

    def html_to_plain_text(self, html_content: str) -> str:
        """
        Convert html to plain text document.

        Args:
            html_content (str): the html string to convert.

        Returns:
            str: the plain text string.
        """
        processor = html2text.HTML2Text()
        return processor.handle(html_content)

    def compile_message(
        self,
        sender: str,
        receiver: str,
        subject: str,
        plain_text_message: str,
        html_message: str,
    ) -> MIMEMultipart:
        """
        Compile the arguments into an
        MIMEMultipart message object.

        Args:
            sender (str): email address to use as sender.
            receiver (str): email address to use as reciever.
            subject (str): message subject line.
            plain_text_message (str): plain text message content.
            html_message (str): html message content.

        Returns:
            MIMEMultipart: The MIMEMultipart email object.
        """

        message = MIMEMultipart("alternative")
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = subject

        message.attach(MIMEText(plain_text_message, "plain", "utf-8"))
        message.attach(MIMEText(html_message, "html", "utf-8"))

        return message

    async def compile_and_send(
        self, filepath: Path, receiver: str, subject: str, **kwargs: dict[str, Any]
    ):
        """
        Compile email from html and send it as html
        with a plaintext alternative.

        Args:
            filepath (Path): path of the html content.
            receiver (str): recipient address.
            subject (str): subject line of the message.
            kwargs (dict[str, Any]): arguments to insert into html.
        """

        html_content = await read_file_async(filepath=filepath)
        html_content = self.template_html(html_content=html_content, **kwargs)
        plain_text_content = self.html_to_plain_text(html_content)
        message = self.compile_message(
            sender=self.sender,
            receiver=receiver,
            subject=subject,
            plain_text_message=plain_text_content,
            html_message=html_content,
        )
        await self.send(message=message)

    async def send(self, message: MIMEMultipart) -> None:
        """
        Send the email using the client.

        Args:
            message (MIMEMultipart): the email object to send.
        """
        raise NotImplementedError
