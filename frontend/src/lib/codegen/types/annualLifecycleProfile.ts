/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { AnnualLifecycleProfileFirstToLastHarvest } from './annualLifecycleProfileFirstToLastHarvest';
import type { AnnualLifecycleProfileGermToFirstHarvest } from './annualLifecycleProfileGermToFirstHarvest';
import type { AnnualLifecycleProfileGermToTransplant } from './annualLifecycleProfileGermToTransplant';
import type { AnnualLifecycleProfileSeedToGerm } from './annualLifecycleProfileSeedToGerm';

export interface AnnualLifecycleProfile {
	first_to_last_harvest?: AnnualLifecycleProfileFirstToLastHarvest;
	germ_to_first_harvest?: AnnualLifecycleProfileGermToFirstHarvest;
	germ_to_transplant?: AnnualLifecycleProfileGermToTransplant;
	seed_to_germ?: AnnualLifecycleProfileSeedToGerm;
}
