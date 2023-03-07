/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Team } from '../models/Team';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TeamService {

    /**
     * Read All
     * @param year
     * @returns Team Successful Response
     * @throws ApiError
     */
    public static teamReadAll(
        year?: number,
    ): CancelablePromise<Array<Team>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/team/all',
            query: {
                'year': year,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
