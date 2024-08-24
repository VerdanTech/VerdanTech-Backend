/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { CultivarAttributeSet } from './cultivarAttributeSet'
import type { CultivarId } from './cultivarId'
import type { CultivarParentId } from './cultivarParentId'

export interface Cultivar {
	attributes?: CultivarAttributeSet
	created_at?: string
	id?: CultivarId
	key: string
	name: string
	parent_id?: CultivarParentId
}
