/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import { faker } from '@faker-js/faker';
import { HttpResponse, delay, http } from 'msw';
import type {
	Coordinate,
	EllipseAttributes,
	LinesAttributes,
	PolygonAttributes,
	WorkspaceFullSchema,
	WorkspacePartialSchema
} from '../../types';

export const getWorkspaceGetFullQueryOpResponsePolygonAttributesMock = (
	overrideResponse: Partial<PolygonAttributes> = {}
): PolygonAttributes => ({
	...{
		hole_polygons: Array.from(
			{ length: faker.number.int({ min: 1, max: 10 }) },
			(_, i) => i + 1
		).map(() =>
			Array.from(
				{ length: faker.number.int({ min: 1, max: 10 }) },
				(_, i) => i + 1
			).map(() => ({
				x: faker.number.int({ min: undefined, max: undefined }),
				y: faker.number.int({ min: undefined, max: undefined }),
				z: faker.helpers.arrayElement([
					faker.helpers.arrayElement([
						null,
						faker.number.int({ min: undefined, max: undefined })
					]),
					undefined
				])
			}))
		),
		shell_coordinates: Array.from(
			{ length: faker.number.int({ min: 1, max: 10 }) },
			(_, i) => i + 1
		).map(() => ({
			x: faker.number.int({ min: undefined, max: undefined }),
			y: faker.number.int({ min: undefined, max: undefined }),
			z: faker.helpers.arrayElement([
				faker.helpers.arrayElement([
					null,
					faker.number.int({ min: undefined, max: undefined })
				]),
				undefined
			])
		}))
	},
	...overrideResponse
});

export const getWorkspaceGetFullQueryOpResponseLinesAttributesMock = (
	overrideResponse: Partial<LinesAttributes> = {}
): LinesAttributes => ({
	...{
		coordinates: Array.from(
			{ length: faker.number.int({ min: 1, max: 10 }) },
			(_, i) => i + 1
		).map(() => ({
			x: faker.number.int({ min: undefined, max: undefined }),
			y: faker.number.int({ min: undefined, max: undefined }),
			z: faker.helpers.arrayElement([
				faker.helpers.arrayElement([
					null,
					faker.number.int({ min: undefined, max: undefined })
				]),
				undefined
			])
		}))
	},
	...overrideResponse
});

export const getWorkspaceGetFullQueryOpResponseEllipseAttributesMock = (
	overrideResponse: Partial<EllipseAttributes> = {}
): EllipseAttributes => ({
	...{
		height: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				faker.number.int({ min: undefined, max: undefined })
			]),
			undefined
		]),
		width: faker.number.int({ min: undefined, max: undefined })
	},
	...overrideResponse
});

export const getWorkspaceGetFullQueryOpResponseCoordinateMock = (
	overrideResponse: Partial<Coordinate> = {}
): Coordinate => ({
	...{
		x: faker.number.int({ min: undefined, max: undefined }),
		y: faker.number.int({ min: undefined, max: undefined }),
		z: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				faker.number.int({ min: undefined, max: undefined })
			]),
			undefined
		])
	},
	...overrideResponse
});

export const getWorkspaceGetFullQueryOpResponseMock = (
	overrideResponse: Partial<WorkspaceFullSchema> = {}
): WorkspaceFullSchema => ({
	description: faker.word.sample(),
	garden_ref: { id: faker.string.uuid() },
	id: faker.string.uuid(),
	name: faker.word.sample(),
	planting_areas: Array.from(
		{ length: faker.number.int({ min: 1, max: 10 }) },
		(_, i) => i + 1
	).map(() => ({
		depth: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				faker.number.int({ min: undefined, max: undefined })
			]),
			undefined
		]),
		description: faker.word.sample(),
		geometry: {
			attributes: faker.helpers.arrayElement([
				{ ...getWorkspaceGetFullQueryOpResponsePolygonAttributesMock() },
				{ ...getWorkspaceGetFullQueryOpResponseLinesAttributesMock() },
				{ ...getWorkspaceGetFullQueryOpResponseEllipseAttributesMock() }
			]),
			position: {
				x: faker.number.int({ min: undefined, max: undefined }),
				y: faker.number.int({ min: undefined, max: undefined }),
				z: faker.helpers.arrayElement([
					faker.helpers.arrayElement([
						null,
						faker.number.int({ min: undefined, max: undefined })
					]),
					undefined
				])
			},
			type: faker.helpers.arrayElement(['polygon', 'ellipse', 'lines'] as const)
		},
		id: faker.string.uuid(),
		location_history: {
			locations: Array.from(
				{ length: faker.number.int({ min: 1, max: 10 }) },
				(_, i) => i + 1
			).map(() => ({
				position: faker.helpers.arrayElement([
					faker.helpers.arrayElement([
						null,
						{ ...getWorkspaceGetFullQueryOpResponseCoordinateMock() }
					]),
					undefined
				]),
				time: faker.helpers.arrayElement([
					faker.helpers.arrayElement([
						null,
						`${faker.date.past().toISOString().split('.')[0]}Z`
					]),
					undefined
				]),
				workspace_ref: { id: faker.string.uuid() }
			}))
		},
		movable: faker.datatype.boolean(),
		name: faker.word.sample()
	})),
	slug: faker.word.sample(),
	...overrideResponse
});

export const getWorkspaceGetPartialsQueryOpResponseMock =
	(): WorkspacePartialSchema[] =>
		Array.from({ length: faker.number.int({ min: 1, max: 10 }) }, (_, i) => i + 1).map(
			() => ({
				garden_ref: { id: faker.string.uuid() },
				id: faker.string.uuid(),
				name: faker.word.sample(),
				slug: faker.word.sample()
			})
		);

export const getWorkspaceGetFullQueryOpMockHandler = (
	overrideResponse?:
		| WorkspaceFullSchema
		| ((
				info: Parameters<Parameters<typeof http.get>[1]>[0]
		  ) => Promise<WorkspaceFullSchema> | WorkspaceFullSchema)
) => {
	return http.get('*/workspaces/query/get_full', async (info) => {
		await delay(1000);
		return new HttpResponse(
			JSON.stringify(
				overrideResponse !== undefined
					? typeof overrideResponse === 'function'
						? await overrideResponse(info)
						: overrideResponse
					: getWorkspaceGetFullQueryOpResponseMock()
			),
			{
				status: 200,
				headers: {
					'Content-Type': 'application/json'
				}
			}
		);
	});
};

export const getWorkspaceGetPartialsQueryOpMockHandler = (
	overrideResponse?:
		| WorkspacePartialSchema[]
		| ((
				info: Parameters<Parameters<typeof http.get>[1]>[0]
		  ) => Promise<WorkspacePartialSchema[]> | WorkspacePartialSchema[])
) => {
	return http.get('*/workspaces/query/get_partials', async (info) => {
		await delay(1000);
		return new HttpResponse(
			JSON.stringify(
				overrideResponse !== undefined
					? typeof overrideResponse === 'function'
						? await overrideResponse(info)
						: overrideResponse
					: getWorkspaceGetPartialsQueryOpResponseMock()
			),
			{
				status: 200,
				headers: {
					'Content-Type': 'application/json'
				}
			}
		);
	});
};
export const getWorkspacesMock = () => [
	getWorkspaceGetFullQueryOpMockHandler(),
	getWorkspaceGetPartialsQueryOpMockHandler()
];