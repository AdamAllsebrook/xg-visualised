/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Match } from '../models/Match';
import type { Player } from '../models/Player';
import type { Season } from '../models/Season';
import type { Shot } from '../models/Shot';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class PlayerService {

    /**
     * Read
     * @param id
     * @returns Player Successful Response
     * @throws ApiError
     */
    public static playerRead(
        id: number,
    ): CancelablePromise<Player> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/player/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Seasons
     * @param id
     * @returns Season Successful Response
     * @throws ApiError
     */
    public static playerReadSeasons(
        id: number,
    ): CancelablePromise<Array<Season>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/player/{id}/seasons',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Matches
     * @param id
     * @param year
     * @returns Match Successful Response
     * @throws ApiError
     */
    public static playerReadMatches(
        id: number,
        year?: number,
    ): CancelablePromise<Array<Match>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/player/{id}/matches',
            path: {
                'id': id,
            },
            query: {
                'year': year,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Shots
     * @param id
     * @param year
     * @returns Shot Successful Response
     * @throws ApiError
     */
    public static playerReadShots(
        id: number,
        year?: number,
    ): CancelablePromise<Array<Shot>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/player/{id}/shots',
            path: {
                'id': id,
            },
            query: {
                'year': year,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
