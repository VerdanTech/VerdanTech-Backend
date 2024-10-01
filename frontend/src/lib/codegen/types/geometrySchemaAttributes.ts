/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { PolygonAttributes } from './polygonAttributes';
import type { LinesAttributes } from './linesAttributes';
import type { EllipseAttributes } from './ellipseAttributes';

export type GeometrySchemaAttributes =
	| PolygonAttributes
	| LinesAttributes
	| EllipseAttributes;