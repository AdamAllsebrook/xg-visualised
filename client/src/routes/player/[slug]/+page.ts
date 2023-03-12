import { error, type Load } from '@sveltejs/kit';
import { PlayerService } from '$client';
import type { Player, Match, Shot } from '$client';

export const load: Load = async ({ params }) => {
    if (!params.slug) throw error(400, 'Must include a player ID.');

    let id = parseInt(params.slug);

    const [player, matches, shots]: [Player, Match[], Shot[]] = await Promise.all([
        PlayerService.playerRead(id),
        PlayerService.playerReadMatches(id),
        PlayerService.playerReadShots(id)
    ]);

    return {
        player: player,
        matches: matches,
        shots: shots
    };
}
