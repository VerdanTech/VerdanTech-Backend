/**
 * Central file to store descriptions of valid mutation schemas.
 * Collates generated typescript schema metadata from the backend.
 * May be autogenerated as well eventually.
 */
import { z as zod } from 'zod';
import userFields from '$lib/backendSchema/specs/user';

export const userFieldSchemas = {
	username: zod
		.string()
		.min(userFields.username.min_length.value, userFields.username.min_length.message)
		.max(userFields.username.max_length.value, userFields.username.max_length.message)
		.regex(userFields.username.pattern.value, userFields.username.pattern.message)
		.describe(userFields.username.description),
	email: zod
		.string()
		.email('Must be a valid email address')
		.describe('Must be a valid email address'),
	password: zod
		.string()
		.min(userFields.password.min_length.value, userFields.password.min_length.message)
		.max(userFields.password.max_length.value, userFields.password.max_length.message)
		.regex(userFields.password.pattern.value, userFields.password.pattern.message)
		.describe(userFields.password.description)
};
