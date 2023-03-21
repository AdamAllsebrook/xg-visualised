<script lang='ts'>
    import type { Player, Match, Shot, Fixture, Team, SimpleShot } from '$client';

    export let player: Player;
    export let shots: Shot[];
    export let matches: Match[];
    export let fixtures: Fixture[];
    export let teams: Map<string, Team>;
    export let allShotsAgainstFixtures: SimpleShot[];

    $: shotsHome = shots.filter(d => d.h_a === 'h');
    $: prefersHome = shotsHome.length / shots.length > 0.5;

    // h_a is reversed here as it refers to the player taking the shot
    $: fixturesHome = allShotsAgainstFixtures.filter(d => d.h_a == 'a');
</script>

<h3 class='font-bold text-2xl'>Home and Away</h3>
<p>
    {player.player_name} has more shots in his {prefersHome ? 'home' : 'away'} games, with {(Math.max(shotsHome.length / shots.length, 1-shotsHome.length / shots.length) * 100).toFixed(2)}% of his shots.
</p>
<p>
    {player.team_title}'s next opponents have conceded {prefersHome ? (100 - fixturesHome.length / allShotsAgainstFixtures.length * 100).toFixed(2) : (fixturesHome.length / allShotsAgainstFixtures.length * 100).toFixed(2)}% of their shots {prefersHome ? 'away from' : 'at'} home.
</p>
