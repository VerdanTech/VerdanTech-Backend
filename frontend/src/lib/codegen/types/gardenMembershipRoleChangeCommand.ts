/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { GardenMembershipRoleChangeCommandRole } from './gardenMembershipRoleChangeCommandRole'

export interface GardenMembershipRoleChangeCommand {
	garden_id: string
	role: GardenMembershipRoleChangeCommandRole
	user_id: string
}
