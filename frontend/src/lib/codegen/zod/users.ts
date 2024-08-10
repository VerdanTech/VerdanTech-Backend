/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import { z as zod } from 'zod'

/**
 * Registers a new user. Requires email confirmation: False.
 * @summary User registration.
 */
export const userCreateCommandOpBodyPassword1Min = 6

export const userCreateCommandOpBodyPassword1Max = 255

export const userCreateCommandOpBodyPassword1RegExp = new RegExp(
	'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\\W).*$'
)
export const userCreateCommandOpBodyPassword2Min = 6

export const userCreateCommandOpBodyPassword2Max = 255

export const userCreateCommandOpBodyPassword2RegExp = new RegExp(
	'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\\W).*$'
)
export const userCreateCommandOpBodyUsernameMin = 3

export const userCreateCommandOpBodyUsernameMax = 50

export const userCreateCommandOpBodyUsernameRegExp = new RegExp('^[a-zA-Z0-9_]*$')

export const userCreateCommandOpBody = zod.object({
	email_address: zod.string().email(),
	password1: zod
		.string()
		.min(userCreateCommandOpBodyPassword1Min)
		.max(userCreateCommandOpBodyPassword1Max)
		.regex(userCreateCommandOpBodyPassword1RegExp),
	password2: zod
		.string()
		.min(userCreateCommandOpBodyPassword2Min)
		.max(userCreateCommandOpBodyPassword2Max)
		.regex(userCreateCommandOpBodyPassword2RegExp),
	username: zod
		.string()
		.min(userCreateCommandOpBodyUsernameMin)
		.max(userCreateCommandOpBodyUsernameMax)
		.regex(userCreateCommandOpBodyUsernameRegExp)
})

/**
 * Closes an email confirmation and verifies the email address.
 * @summary Email confirmation.
 */
export const userConfirmEmailConfirmationCommandOpBody = zod.object({
	key: zod.string().uuid()
})

/**
 * Requests a new email verification email be sent to the email address.
 * @summary Email confirmation request.
 */
export const userRequestEmailConfirmationCommandOpBody = zod.object({
	email_address: zod.string().email()
})

/**
 * Authenticate the request with JWT cookie authentication.
 * @summary User login
 */
export const userLoginCommandOpBodyPasswordMin = 6

export const userLoginCommandOpBodyPasswordMax = 255

export const userLoginCommandOpBodyPasswordRegExp = new RegExp(
	'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\\W).*$'
)

export const userLoginCommandOpBody = zod.object({
	email_address: zod.string().email(),
	password: zod
		.string()
		.min(userLoginCommandOpBodyPasswordMin)
		.max(userLoginCommandOpBodyPasswordMax)
		.regex(userLoginCommandOpBodyPasswordRegExp)
})

/**
 * Closes a password reset request and changes the password
 * @summary Password reset confirm.
 */
export const userConfirmPasswordResetCommandOpBodyNewPassword1Min = 6

export const userConfirmPasswordResetCommandOpBodyNewPassword1Max = 255

export const userConfirmPasswordResetCommandOpBodyNewPassword1RegExp = new RegExp(
	'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\\W).*$'
)
export const userConfirmPasswordResetCommandOpBodyNewPassword2Min = 6

export const userConfirmPasswordResetCommandOpBodyNewPassword2Max = 255

export const userConfirmPasswordResetCommandOpBodyNewPassword2RegExp = new RegExp(
	'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\\W).*$'
)

export const userConfirmPasswordResetCommandOpBody = zod.object({
	key: zod.string().uuid(),
	new_password1: zod
		.string()
		.min(userConfirmPasswordResetCommandOpBodyNewPassword1Min)
		.max(userConfirmPasswordResetCommandOpBodyNewPassword1Max)
		.regex(userConfirmPasswordResetCommandOpBodyNewPassword1RegExp),
	new_password2: zod
		.string()
		.min(userConfirmPasswordResetCommandOpBodyNewPassword2Min)
		.max(userConfirmPasswordResetCommandOpBodyNewPassword2Max)
		.regex(userConfirmPasswordResetCommandOpBodyNewPassword2RegExp),
	user_id: zod.string().uuid()
})

/**
 * Open a new password reset request and sends confirmation email.
 * @summary Password reset request.
 */
export const userRequestPasswordResetCommandOpBody = zod.object({
	email_address: zod.string().email()
})

/**
 * Returns the profile of the authenticated user.
 * @summary User client profile view.
 */
export const userClientProfileQueryOpResponse = zod.object({
	created_at: zod.string().datetime(),
	emails: zod.array(
		zod.object({
			address: zod.string(),
			primary: zod.boolean(),
			verified: zod.boolean()
		})
	),
	id: zod.string().uuid(),
	is_superuser: zod.boolean(),
	username: zod.string()
})

/**
 * Returns the profiles of the user ids given.
 * @summary User public profiles view.
 */
export const userPublicProfilesQueryOpQueryParams = zod.object({
	user_ids: zod.array(zod.string().uuid())
})

export const userPublicProfilesQueryOpResponseItem = zod.object({
	id: zod.string().uuid(),
	username: zod.string()
})
export const userPublicProfilesQueryOpResponse = zod.array(
	userPublicProfilesQueryOpResponseItem
)