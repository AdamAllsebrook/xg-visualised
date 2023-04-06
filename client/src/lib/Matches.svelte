<script lang="ts">
    import type { Match, Shot } from '$client';
    import type { Spring } from 'svelte/motion';
    import { fade } from 'svelte/transition';
    import { cubicOut } from 'svelte/easing';
    import { key as dataKey, type DataManager } from './data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import { ViewManager, viewKey } from './view/viewManager';
    import HomeAway from './view/content/HomeAway.svelte';
    import { SimpleShotData } from './data/shotData';
    import { key as shotsConcededKey, type LeagueShotsConceded } from './data/leagueShotsConceded';
    import { colours } from './colours';
    import { initSprings } from './initSprings';

    export let width: number;
    export let height: number;
    export let tweenedX: Spring<number[]>;
    export let tweenedY: Spring<number[]>;

    const viewManager: ViewManager = getContext(viewKey);
    const currentStep = viewManager.currentStep;

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const shots: Shot[] = $dataManager.shots;
    const matches: Match[] = $dataManager.matches;

    const teamSelected: Writable<string | null> = viewManager.teamSelected;
    const leagueShotsConceded: Writable<LeagueShotsConceded> = getContext(shotsConcededKey);

    $: shotsConceded = $dataManager.opponents.shotsConceded;
    $: allShotsConceded = shotsConceded == null 
        ? null 
        : $teamSelected == null 
            ? shotsConceded
            : $leagueShotsConceded.data.get($teamSelected) || new SimpleShotData([]);;
    $: shotsConcededList = $dataManager.opponents.shotsConcededList;
    $: allShotsConcededList = shotsConcededList == null 
        ? null 
        : $teamSelected == null 
            ? $dataManager.opponents.shotsConcededList
            : $leagueShotsConceded.teamShots.get($teamSelected) || [];

    $: opponentsMinuteBins = allShotsConcededList === null ? [] : SimpleShotData.minuteBins(allShotsConcededList);
    $: opponentsMinuteXgs = opponentsMinuteBins.map((bin) => bin.xG);

    const minuteBins = SimpleShotData.minuteBins($dataManager.shots);
    const minuteXgs = minuteBins.map((bin) => bin.xG);
    // argmax
    const preferTime = minuteXgs.indexOf(Math.max(...minuteXgs));

    $: paddingY = height / (matches.length + 1);
    $: matchesSorted = matches.sort((a, b) => Date.parse(a.date) - Date.parse(b.date));
    $: matchesMap = new Map(matchesSorted.map((match, i) => [match.id, i]));

    $: {
        scale;
        if (!tweenedX && scale) {
            let xs = shots.map((shot) => scale(shot).x);
            let ys = shots.map((shot) => scale(shot).y);
            [tweenedX, tweenedY] = initSprings(xs, ys);
        }
    }
    $: scale = (shot: Shot) => {
        return {
            x: (Math.min(shot.minute, 90) * width) / 90,
            y: (matchesMap.get(shot.match_id) || 0) * paddingY,
        };
    };

    $: {
        scale, $currentStep;
        tweenedX.set(shots.map((shot) => scale(shot).x));
        tweenedY.set(shots.map((shot) => scale(shot).y));
    }
</script>

<g transition:fade={{ delay: 0, duration: 300, easing: cubicOut }}>
    {#each matchesSorted as match, i}
        <line
            x1="0"
            x2={(match.time_started * width) / 90}
            y1={Math.round(i * paddingY)}
            y2={Math.round(i * paddingY)}
            stroke="{viewManager.steps[$currentStep || 0].shotLayout === 'homeaway' 
                ? match.h_a === 'h'
                    ? '#aaa9'
                    : '#aaa3'
                : '#aaa6'}"
            stroke-width="1"
            style='transition: stroke 0.2s'
        />
        <rect
            x={(match.time_started * width) / 90}
            width={(match.time * width) / 90}
            y={Math.round(i * paddingY) - 3}
            height="6"
            rx="2"
            stroke="black"
            stroke-width="1"
            fill="{viewManager.steps[$currentStep || 0].shotLayout === 'homeaway' 
                ? match.h_a === 'h'
                    ? '#aaa9'
                    : '#aaa3'
                : '#aaa6'}"
            style='transition: fill 0.2s'
        />
        <line
            x1={((match.time_started + match.time) * width) / 90}
            x2={width}
            y1={Math.round(i * paddingY)}
            y2={Math.round(i * paddingY)}
            stroke-width="1"
            stroke="{viewManager.steps[$currentStep || 0].shotLayout === 'homeaway' 
                ? match.h_a === 'h'
                    ? '#aaa9'
                    : '#aaa3'
                : '#aaa6'}"
            style='transition: stroke 0.2s'
        />
    {/each}
    {#if viewManager.steps[$currentStep || 0].shotLayout === 'minutes'}
        <rect
            x={preferTime * 15 * (width / 90)}
            width={15 * (width / 90)}
            y={-paddingY / 2}
            height={height * (1 - 1 / (matches.length + 1))}
            rx="2"
            stroke="black"
            stroke-width="1"
            fill="#aaa3"
            style='transition: fill 0.2s'
            transition:fade={{ delay: 0, duration: 150, easing: cubicOut }}
        />
    {/if}
    {#if allShotsConcededList !== null && viewManager.steps[$currentStep || 0].opponentsInfo === 'minutes'}
        {#each opponentsMinuteXgs as xg, i}
            <rect
                x={i * 15 * (width / 90) + 5}
                width={15 * (width / 90) - 10}
                y={-paddingY / 2}
                height={3 * height * (1 - 1 / (matches.length + 1)) * (allShotsConceded === null ? 0 : xg / allShotsConceded.xG)}
                rx="2"
                stroke="black"
                stroke-width="1"
                fill="{colours.xg}99"
                style='transition: fill 0.2s; transition: height 0.15s'
                transition:fade={{ delay: 0, duration: 150, easing: cubicOut }}
            />
        {/each}
    {/if}
</g>
