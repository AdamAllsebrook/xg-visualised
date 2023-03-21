<script lang='ts'>
    import type { Player, Match, Shot, Fixture, Team, SimpleShot } from '$client';

    export let player: Player;
    export let shots: Shot[];
    export let matches: Match[];
    export let fixtures: Fixture[];
    export let teams: Map<string, Team>;
    export let allShotsAgainstFixtures: SimpleShot[];

    $: firstHalfShots = shots.filter(d => d.minute <= 45);
    $: firstHalfPercent = firstHalfShots.length / shots.length * 100;
    $: prefersFirstHalf = firstHalfPercent > 50;

    $: fixturesFirstHalf = allShotsAgainstFixtures.filter(d => d.minute >= 45);
    $: fixturesFirstHalfPercent = fixturesFirstHalf.length / allShotsAgainstFixtures.length * 100;
</script>

<h3 class='font-bold text-2xl'>First or Second Half</h3>
<p>
    {player.player_name} has more luck in the {prefersFirstHalf ? 'first' : 'second'} half, with {Math.max(firstHalfPercent, 100 - firstHalfPercent).toFixed(2)}% of his shots.
</p>
<p>
    {player.team_title}'s next opponents have conceded {prefersFirstHalf ? fixturesFirstHalfPercent.toFixed(2) : (100 - fixturesFirstHalfPercent).toFixed(2)}% of their shots in the {prefersFirstHalf ? 'first' : 'second'} half.
</p>
