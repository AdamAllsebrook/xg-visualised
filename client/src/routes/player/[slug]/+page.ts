import { error, type Load } from '@sveltejs/kit';
import { team } from './store.js';
import { PlayerService, TeamService } from '$client';

export const load: Load = async ({ params }) => {
    if (!params.slug) throw error(400, 'Must include a player ID.');

    let id = parseInt(params.slug);
    const player = await PlayerService.playerRead(id);
    TeamService.teamRead(player.team)
        .then(data => team.set(data));
    return player;
}