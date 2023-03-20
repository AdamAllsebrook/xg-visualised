
<script lang='ts'>
    import { getContext } from 'svelte';
    import type { Player, Match, Shot, Fixture, Team, SimpleShot } from '$client';
    import FixtureList from '$lib/FixtureList.svelte';

    export let player: Player;
    export let shots: Shot[];
    export let matches: Match[];
    export let fixtures: Fixture[];
    export let teams: Map<string, Team>;
    export let allShotsAgainstFixtures: SimpleShot[];

    function isLeft(shot: Shot | SimpleShot) {
        return shot.Y > 0.5
    }

    $: leftShots = shots.filter(d => isLeft(d));
    $: prefersLeft = leftShots.length / shots.length > 0.5;

    $: fixturesLeftShots = allShotsAgainstFixtures.filter(d => isLeft(d));
</script>

<h3 class='font-bold text-2xl'>Left or Right?</h3>
<p>
    {player.player_name} prefers shooting from the {prefersLeft ? 'left' : 'right'} side, with {(Math.max(leftShots.length / shots.length, 1 - leftShots.length / shots.length) * 100).toFixed(2)}% of his shots coming from that side of the pitch.
</p>
<p>
   {player.team_title}'s next opponents have conceded {(leftShots.length / shots.length > 0.5 ? fixturesLeftShots.length / allShotsAgainstFixtures.length * 100 : 100 - fixturesLeftShots.length / allShotsAgainstFixtures.length * 100).toFixed(0)}% of their total shots conceded from the {leftShots.length / shots.length > 0.5 ? 'left' : 'right'} side of the box. 
</p>
