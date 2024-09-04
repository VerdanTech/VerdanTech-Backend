/**
 * Central file to store descriptions of valid mutation schemas.
 * Collates generated typescript schema metadata from the backend.
 * May be autogenerated as well eventually.
 */
import { z as zod } from 'zod';
import gardenFields from '$lib/backendSchema/specs/garden';
import { GardenCreateCommandVisibility } from '$codegen/types';

export const gardenFieldSchemas = {
	name: zod
		.string()
		.min(
			gardenFields.garden_name.min_length.value,
			gardenFields.garden_name.min_length.message
		)
		.max(
			gardenFields.garden_name.max_length.value,
			gardenFields.garden_name.max_length.message
		)
		.regex(
			gardenFields.garden_name.pattern.value,
			gardenFields.garden_name.pattern.message
		)
		.describe(gardenFields.garden_name.description),
	key: zod
		.string()
		.min(
			gardenFields.garden_key.min_length.value,
			gardenFields.garden_key.min_length.message
		)
		.max(
			gardenFields.garden_key.max_length.value,
			gardenFields.garden_key.max_length.message
		)
		.regex(
			gardenFields.garden_key.pattern.value,
			gardenFields.garden_key.pattern.message
		)
		.describe(gardenFields.garden_key.description),
	description: zod
		.string()
		.max(
			gardenFields.garden_description.max_length.value,
			gardenFields.garden_description.max_length.message
		)
		.describe(gardenFields.garden_description.description),
	visibility: zod.nativeEnum(GardenCreateCommandVisibility),
	user_invites_list: zod
		.array(zod.string())
		.max(
			gardenFields.user_invites_list.max_length.value,
			gardenFields.user_invites_list.max_length.message
		)
		.describe(gardenFields.user_invites_list.description)
};
