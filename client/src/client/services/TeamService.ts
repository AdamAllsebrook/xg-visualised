/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Fixture } from '../models/Fixture';
import type { Result } from '../models/Result';
import type { Team } from '../models/Team';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TeamService {

    /**
     * Read
     * @param id
     * @returns Team Successful Response
     * @throws ApiError
     */
    public static teamRead(
        id: number,
    ): CancelablePromise<Team> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/team/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Results
     * @param id
     * @returns Result Successful Response
     * @throws ApiError
     */
    public static teamReadResults(
        id: number,
    ): CancelablePromise<Array<Result>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/team/{id}/results',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Fixtures
     * @param id
     * @returns Fixture Successful Response
     * @throws ApiError
     */
    public static teamReadFixtures(
        id: number,
    ): CancelablePromise<Array<Fixture>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/team/{id}/fixtures',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
