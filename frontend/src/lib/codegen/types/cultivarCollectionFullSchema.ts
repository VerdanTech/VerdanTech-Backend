/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { CultivarSchema } from './cultivarSchema';
import type { CultivarCollectionFullSchemaGardenRef } from './cultivarCollectionFullSchemaGardenRef';
import type { CultivarCollectionFullSchemaParentRef } from './cultivarCollectionFullSchemaParentRef';
import type { CultivarCollectionFullSchemaUserRef } from './cultivarCollectionFullSchemaUserRef';
import type { CultivarCollectionFullSchemaVisibility } from './cultivarCollectionFullSchemaVisibility';

export interface CultivarCollectionFullSchema {
	created_at: string;
	cultivars: CultivarSchema[];
	description: string;
	garden_ref?: CultivarCollectionFullSchemaGardenRef;
	id: string;
	name: string;
	parent_ref?: CultivarCollectionFullSchemaParentRef;
	slug: string;
	tags: string[];
	user_ref?: CultivarCollectionFullSchemaUserRef;
	visibility: CultivarCollectionFullSchemaVisibility;
}
