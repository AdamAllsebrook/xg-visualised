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

    function isInBox(shot: Shot | SimpleShot) {
        return shot.Y > 15/74 && shot.Y < 59/74 && shot.X > 97/115
    }

    $: shotsInBox = shots.filter(d => isInBox(d));
    $: shotsOutBox = shots.filter(d => !isInBox(d));

    $: fixturesShotsInBox = allShotsAgainstFixtures.filter(d => isInBox(d));
</script>

<h3 class='font-bold text-2xl'>Fox in the Box</h3>
<p>
    Of {player.player_name}'s {shots.length} shots, {Math.max(shotsInBox.length, shotsOutBox.length)} ({(Math.max(shotsInBox.length, shotsOutBox.length) / shots.length * 100).toFixed(0)}%) were from {shotsInBox.length > shotsOutBox.length ? 'inside' : 'outside'} of the box.
</p>
<p>
   {player.team_title}'s next opponents have conceded {(shotsInBox.length > shotsOutBox.length ? fixturesShotsInBox.length / allShotsAgainstFixtures.length * 100 : 100 - fixturesShotsInBox.length / allShotsAgainstFixtures.length * 100).toFixed(0)}% of their total shots conceded from {shotsInBox.length > shotsOutBox.length ? 'inside' : 'outside'} of the box. 
</p>
