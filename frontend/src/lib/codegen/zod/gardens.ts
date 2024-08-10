/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import { z as zod } from 'zod'

/**
 * Accepts a Garden Membership.
 * @summary Garden membership invitiation acceptance.
 */
export const gardenMembershipAcceptCommandOpBodyGardenKeyMin = 4

export const gardenMembershipAcceptCommandOpBodyGardenKeyMax = 16

export const gardenMembershipAcceptCommandOpBodyGardenKeyRegExp = new RegExp(
	'[0-9A-Za-z-]+'
)

export const gardenMembershipAcceptCommandOpBody = zod.object({
	garden_key: zod
		.string()
		.min(gardenMembershipAcceptCommandOpBodyGardenKeyMin)
		.max(gardenMembershipAcceptCommandOpBodyGardenKeyMax)
		.regex(gardenMembershipAcceptCommandOpBodyGardenKeyRegExp)
})

/**
 * Changes the role on another's Garden Membership.
 * @summary Garden Membership role change.
 */
export const gardenMembershipRoleChangeCommandOpBody = zod.object({
	garden_id: zod.string().uuid(),
	role: zod.enum(['admin', 'editor', 'viewer']),
	user_id: zod.string().uuid()
})

/**
 * Creates a new Garden and invites requested users.
 * @summary Garden creation.
 */
export const gardenCreateCommandOpBodyDescriptionMax = 1400
export const gardenCreateCommandOpBodyNameMin = 2

export const gardenCreateCommandOpBodyNameMax = 50

export const gardenCreateCommandOpBodyNameRegExp = new RegExp('[0-9A-Za-z ]+')

/**
 * Creates new Garden Memberships and sends email confirmation emails.
 * @summary Garden membership invitiation.
 */
export const gardenMembershipCreateCommandOpBody = zod.object({
	admin_ids: zod.array(zod.string().uuid()).optional(),
	editor_ids: zod.array(zod.string().uuid()).optional(),
	garden_id: zod.string().uuid(),
	viewer_ids: zod.array(zod.string().uuid()).optional()
})

/**
 * Removes one's own Garden Membership from a garden.
 * @summary Garden membership deletion.
 */
export const gardenMembershipDeleteCommandOpBodyGardenKeyMin = 4

export const gardenMembershipDeleteCommandOpBodyGardenKeyMax = 16

export const gardenMembershipDeleteCommandOpBodyGardenKeyRegExp = new RegExp(
	'[0-9A-Za-z-]+'
)
