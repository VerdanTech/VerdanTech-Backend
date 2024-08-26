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
	CultivarCollectionFullSchema,
	CultivarGetByClientResult,
	CultivarGetByGardenResult,
	FrostDatePlantingWindowProfile,
	RefSchema
} from '../../types';

export const getCultivarAttributeUpdateCommandOpResponseMock = (): string =>
	faker.word.sample();

export const getCultivarGetByClientQueryOpResponseRefSchemaMock = (
	overrideResponse: Partial<RefSchema> = {}
): RefSchema => ({ ...{ id: faker.string.uuid() }, ...overrideResponse });

export const getCultivarGetByClientQueryOpResponseMock = (
	overrideResponse: Partial<CultivarGetByClientResult> = {}
): CultivarGetByClientResult => ({
	collections: Array.from(
		{ length: faker.number.int({ min: 1, max: 10 }) },
		(_, i) => i + 1
	).map(() => ({
		description: faker.word.sample(),
		garden_ref: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				{ ...getCultivarGetByClientQueryOpResponseRefSchemaMock() }
			]),
			undefined
		]),
		id: faker.string.uuid(),
		key: faker.word.sample(),
		name: faker.word.sample(),
		parent_ref: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				{ ...getCultivarGetByClientQueryOpResponseRefSchemaMock() }
			]),
			undefined
		]),
		tags: Array.from(
			{ length: faker.number.int({ min: 1, max: 10 }) },
			(_, i) => i + 1
		).map(() => faker.word.sample()),
		user_ref: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				{ ...getCultivarGetByClientQueryOpResponseRefSchemaMock() }
			]),
			undefined
		])
	})),
	...overrideResponse
});

export const getCultivarGetByGardenQueryOpResponseRefSchemaMock = (
	overrideResponse: Partial<RefSchema> = {}
): RefSchema => ({ ...{ id: faker.string.uuid() }, ...overrideResponse });

export const getCultivarGetByGardenQueryOpResponseMock = (
	overrideResponse: Partial<CultivarGetByGardenResult> = {}
): CultivarGetByGardenResult => ({
	active_collection: { id: faker.string.uuid() },
	collections: Array.from(
		{ length: faker.number.int({ min: 1, max: 10 }) },
		(_, i) => i + 1
	).map(() => ({
		description: faker.word.sample(),
		garden_ref: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				{ ...getCultivarGetByGardenQueryOpResponseRefSchemaMock() }
			]),
			undefined
		]),
		id: faker.string.uuid(),
		key: faker.word.sample(),
		name: faker.word.sample(),
		parent_ref: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				{ ...getCultivarGetByGardenQueryOpResponseRefSchemaMock() }
			]),
			undefined
		]),
		tags: Array.from(
			{ length: faker.number.int({ min: 1, max: 10 }) },
			(_, i) => i + 1
		).map(() => faker.word.sample()),
		user_ref: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				{ ...getCultivarGetByGardenQueryOpResponseRefSchemaMock() }
			]),
			undefined
		])
	})),
	...overrideResponse
});

export const getCultivarGetByIdsQueryOpResponseFrostDatePlantingWindowProfileMock = (
	overrideResponse: Partial<FrostDatePlantingWindowProfile> = {}
): FrostDatePlantingWindowProfile => ({
	...{
		first_frost_window_close: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				faker.number.int({ min: undefined, max: undefined })
			]),
			undefined
		]),
		first_frost_window_open: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				faker.number.int({ min: undefined, max: undefined })
			]),
			undefined
		]),
		last_frost_window_close: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				faker.number.int({ min: undefined, max: undefined })
			]),
			undefined
		]),
		last_frost_window_open: faker.helpers.arrayElement([
			faker.helpers.arrayElement([
				null,
				faker.number.int({ min: undefined, max: undefined })
			]),
			undefined
		])
	},
	...overrideResponse
});

export const getCultivarGetByIdsQueryOpResponseRefSchemaMock = (
	overrideResponse: Partial<RefSchema> = {}
): RefSchema => ({ ...{ id: faker.string.uuid() }, ...overrideResponse });

export const getCultivarGetByIdsQueryOpResponseMock =
	(): CultivarCollectionFullSchema[] =>
		Array.from({ length: faker.number.int({ min: 1, max: 10 }) }, (_, i) => i + 1).map(
			() => ({
				cultivars: Array.from(
					{ length: faker.number.int({ min: 1, max: 10 }) },
					(_, i) => i + 1
				).map(() => ({
					attributes: {
						frost_date_planting_window_profile: faker.helpers.arrayElement([
							faker.helpers.arrayElement([
								null,
								{
									...getCultivarGetByIdsQueryOpResponseFrostDatePlantingWindowProfileMock()
								}
							]),
							undefined
						])
					},
					id: faker.string.uuid(),
					key: faker.word.sample(),
					name: faker.word.sample(),
					parent_id: faker.helpers.arrayElement([
						faker.helpers.arrayElement([null, faker.string.uuid()]),
						undefined
					])
				})),
				description: faker.helpers.arrayElement([
					faker.helpers.arrayElement([null, faker.word.sample()]),
					undefined
				]),
				garden_ref: faker.helpers.arrayElement([
					faker.helpers.arrayElement([
						null,
						{ ...getCultivarGetByIdsQueryOpResponseRefSchemaMock() }
					]),
					undefined
				]),
				id: faker.string.uuid(),
				key: faker.word.sample(),
				name: faker.word.sample(),
				parent_ref: faker.helpers.arrayElement([
					faker.helpers.arrayElement([
						null,
						{ ...getCultivarGetByIdsQueryOpResponseRefSchemaMock() }
					]),
					undefined
				]),
				tags: Array.from(
					{ length: faker.number.int({ min: 1, max: 10 }) },
					(_, i) => i + 1
				).map(() => faker.word.sample()),
				user_ref: faker.helpers.arrayElement([
					faker.helpers.arrayElement([
						null,
						{ ...getCultivarGetByIdsQueryOpResponseRefSchemaMock() }
					]),
					undefined
				])
			})
		);

export const getCultivarAttributeUpdateCommandOpMockHandler = () => {
	return http.post('*/cultivars/command/update', async () => {
		await delay(1000);
		return new HttpResponse(getCultivarAttributeUpdateCommandOpResponseMock(), {
			status: 201,
			headers: {
				'Content-Type': 'text/plain'
			}
		});
	});
};

export const getCultivarGetByClientQueryOpMockHandler = (
	overrideResponse?:
		| CultivarGetByClientResult
		| ((
				info: Parameters<Parameters<typeof http.get>[1]>[0]
		  ) => Promise<CultivarGetByClientResult> | CultivarGetByClientResult)
) => {
	return http.get('*/cultivars/query/get_by_client', async (info) => {
		await delay(1000);
		return new HttpResponse(
			JSON.stringify(
				overrideResponse !== undefined
					? typeof overrideResponse === 'function'
						? await overrideResponse(info)
						: overrideResponse
					: getCultivarGetByClientQueryOpResponseMock()
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

export const getCultivarGetByGardenQueryOpMockHandler = (
	overrideResponse?:
		| CultivarGetByGardenResult
		| ((
				info: Parameters<Parameters<typeof http.get>[1]>[0]
		  ) => Promise<CultivarGetByGardenResult> | CultivarGetByGardenResult)
) => {
	return http.get('*/cultivars/query/get_by_garden', async (info) => {
		await delay(1000);
		return new HttpResponse(
			JSON.stringify(
				overrideResponse !== undefined
					? typeof overrideResponse === 'function'
						? await overrideResponse(info)
						: overrideResponse
					: getCultivarGetByGardenQueryOpResponseMock()
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

export const getCultivarGetByIdsQueryOpMockHandler = (
	overrideResponse?:
		| CultivarCollectionFullSchema[]
		| ((
				info: Parameters<Parameters<typeof http.get>[1]>[0]
		  ) => Promise<CultivarCollectionFullSchema[]> | CultivarCollectionFullSchema[])
) => {
	return http.get('*/cultivars/query/get_by_ids', async (info) => {
		await delay(1000);
		return new HttpResponse(
			JSON.stringify(
				overrideResponse !== undefined
					? typeof overrideResponse === 'function'
						? await overrideResponse(info)
						: overrideResponse
					: getCultivarGetByIdsQueryOpResponseMock()
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
export const getCultivarsMock = () => [
	getCultivarAttributeUpdateCommandOpMockHandler(),
	getCultivarGetByClientQueryOpMockHandler(),
	getCultivarGetByGardenQueryOpMockHandler(),
	getCultivarGetByIdsQueryOpMockHandler()
];