import { error, type Load } from '@sveltejs/kit';
import { PlayerService, TeamService, type SimpleShot } from '$client';
import type { Player, Match, Shot, Fixture, Team } from '$client';
import { YEAR } from '$env/static/private'

export const load: Load = async ({ url, params }) => {
    if (!params.slug) throw error(400, 'Must include a player ID.');
    let year = url.searchParams.get('year');
    if (year === null || year.length === 0) {
        if (YEAR === undefined) {
            year = '2022';
        }
        else {
            year = YEAR;
        }
    }

    const id = parseInt(params.slug);
    const yearInt = parseInt(year as string);

    const [player, matches, shots, fixtures, teams]: [
        Player,
        Match[],
        Shot[],
        Fixture[],
        Team[],
    ] = await Promise.all([
        PlayerService.playerRead(id, yearInt),
        PlayerService.playerReadMatches(id, yearInt),
        PlayerService.playerReadShots(id, yearInt),
        PlayerService.playerReadFixtures(id, yearInt),
        TeamService.teamReadAll(yearInt),
    ]);

    return {
        data: [player, shots, teams, matches, fixtures],
        streamed: {
            shotsAgainst: await PlayerService.playerReadAllShots(yearInt),
        }
    };
};
