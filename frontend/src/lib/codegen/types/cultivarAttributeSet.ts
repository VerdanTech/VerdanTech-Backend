/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { AnnualLifecycleProfile } from './annualLifecycleProfile';
import type { FrostDatePlantingWindowProfile } from './frostDatePlantingWindowProfile';
import type { OriginProfile } from './originProfile';

export interface CultivarAttributeSet {
	annual_lifecycle_profile?: AnnualLifecycleProfile;
	frost_date_planting_window_profile?: FrostDatePlantingWindowProfile;
	origin_profile?: OriginProfile;
}
