<script lang="ts">
	import { Command as CommandPrimitive } from 'cmdk-sv';
	import { cn } from '$lib/utils';

	type $$Props = CommandPrimitive.ItemProps;

	export let asChild = false;

	let className: string | undefined | null = undefined;
	export { className as class };
</script>

<CommandPrimitive.Item
	{asChild}
	class={cn(
		'relative flex cursor-default select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none aria-selected:bg-accent-6 aria-selected:text-accent-12 data-[disabled]:pointer-events-none data-[disabled]:opacity-50',
		className
	)}
	{...$$restProps}
	let:action
	let:attrs
>
	<slot {action} {attrs} />
</CommandPrimitive.Item>
