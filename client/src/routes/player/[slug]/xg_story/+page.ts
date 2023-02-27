import { error, type Load } from '@sveltejs/kit';
import { matches, seasons, shots, team } from '../store.js';
import { PlayerService, TeamService } from '$client';

export const load: Load = async ({ params }) => {
    if (!params.slug) throw error(400, 'Must include a player ID.');

    matches.set([]);
    seasons.set([]);
    shots.set([]);
    team.set({
        id: 0,
        name: ''
    })

    let id = parseInt(params.slug);
    const player = await PlayerService.playerRead(id);
    PlayerService.playerReadMatches(id)
        .then(data => matches.set(data));
    PlayerService.playerReadSeasons(id)
        .then(data => seasons.set(data));
    PlayerService.playerReadShots(id)
        .then(data => shots.set(data));
    TeamService.teamRead(player.team)
        .then(data => team.set(data));
    return player;
}