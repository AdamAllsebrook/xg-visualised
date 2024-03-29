import type { Load } from '@sveltejs/kit';
import { ItemsService } from '$client';
import { YEAR } from '$env/static/private'

export const load: Load = async ({ url }) => {
    let year = url.searchParams.get('year');
    if (year === null || year.length === 0) {
        if (YEAR === undefined) {
            year = '2022';
        }
        else {
            year = YEAR;
        }
    }
    const yearInt = parseInt(year as string);

    const start = Date.now();
    const items = await ItemsService.itemsRead(yearInt);
    const end = Date.now();
    console.log(`Request time (get items): ${end - start} ms`);

    return {
        items: items
    };
};
