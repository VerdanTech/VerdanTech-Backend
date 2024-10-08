/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { CultivarUpdateCommandAttributes } from './cultivarUpdateCommandAttributes';
import type { CultivarUpdateCommandDescription } from './cultivarUpdateCommandDescription';
import type { CultivarUpdateCommandKey } from './cultivarUpdateCommandKey';
import type { CultivarUpdateCommandNames } from './cultivarUpdateCommandNames';
import type { CultivarUpdateCommandParentId } from './cultivarUpdateCommandParentId';
import type { CultivarUpdateCommandScientificName } from './cultivarUpdateCommandScientificName';

export interface CultivarUpdateCommand {
	attributes?: CultivarUpdateCommandAttributes;
	collection_ref: string;
	cultivar_id: string;
	description?: CultivarUpdateCommandDescription;
	key?: CultivarUpdateCommandKey;
	names?: CultivarUpdateCommandNames;
	parent_id?: CultivarUpdateCommandParentId;
	remove_parent?: boolean;
	scientific_name?: CultivarUpdateCommandScientificName;
}
