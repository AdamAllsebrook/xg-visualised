/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { PlayerSearch } from '../models/PlayerSearch';
import type { TeamSearch } from '../models/TeamSearch';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class ItemsService {

    /**
     * Read
     * @returns any Successful Response
     * @throws ApiError
     */
    public static itemsRead(): CancelablePromise<Array<(PlayerSearch | TeamSearch)>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/items/',
        });
    }

}
