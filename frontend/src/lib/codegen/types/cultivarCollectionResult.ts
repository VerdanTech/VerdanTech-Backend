/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { CultivarResult } from './cultivarResult'
import type { RefSchema } from './refSchema'

export interface CultivarCollectionResult {
	cultivars: CultivarResult[]
	description: string
	garden_ref: RefSchema
	key: string
	name: string
	parent_ref: RefSchema
	tags: string[]
	user_ref: RefSchema
}
