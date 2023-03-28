import { error, type Load } from '@sveltejs/kit';
import { PlayerService, TeamService } from '$client';
import type { Player, Match, Shot, Fixture, Team } from '$client';
import { DataManager } from '$lib/data/dataManager';

export const load: Load = async ({ params }) => {
    if (!params.slug) throw error(400, 'Must include a player ID.');

    let id = parseInt(params.slug);

    const [player, matches, shots, fixtures, teams]: [Player, Match[], Shot[], Fixture[], Team[]] = await Promise.all([
        PlayerService.playerRead(id),
        PlayerService.playerReadMatches(id),
        PlayerService.playerReadShots(id),
        PlayerService.playerReadFixtures(id),
        TeamService.teamReadAll() 
    ]);

    return {
        data: new DataManager(
            player,
            shots,
            teams,
            matches,
            fixtures
        )
    };
}
