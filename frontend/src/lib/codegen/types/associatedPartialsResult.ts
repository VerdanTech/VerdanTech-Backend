/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { GardenPartialSchema } from './gardenPartialSchema'

export interface AssociatedPartialsResult {
	admin_memberships: GardenPartialSchema[]
	edit_memberships: GardenPartialSchema[]
	favorites: GardenPartialSchema[]
	pending_memberships: GardenPartialSchema[]
	recently_viewed: GardenPartialSchema[]
	view_memberships: GardenPartialSchema[]
}
