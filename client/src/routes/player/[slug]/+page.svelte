<script lang="ts">
    import { onMount } from 'svelte';
    import type { Spring } from 'svelte/motion';
    import { setContext } from 'svelte';
    import { writable, type Writable } from 'svelte/store';
    import { scaleLinear } from 'd3-scale';

    import Scrolly from '$lib/Scrolly.svelte';
    import Tooltip from '$lib/Tooltip.svelte';
    import VizContainer from '$lib/VizContainer.svelte';
    import XgCircles from '$lib/XgCircles.svelte';
    import ContentManager from '$lib/ContentManager.svelte';
    import VizManager from '$lib/VizManager.svelte';
    import type { Margin } from '$lib/margin';
    import { DataManager, key as dataKey } from '$lib/data/dataManager';
    import { HoveredDataType } from '$lib/view/hoveredData';

    import Title from './Title.svelte';
    import { leagueShotsConceded } from './stores.js';
    import { LeagueShotsConceded, key as concedeKey } from '$lib/data/leagueShotsConceded';
    import { ViewManager, viewKey } from '$lib/view/viewManager';

    export let data: any;
    const dataManager: Writable<DataManager> = writable(new DataManager(...data.data));
    setContext(dataKey, dataManager);
    setContext(concedeKey, leagueShotsConceded);

    let isMounted = false;

    let screenWidth: number;
    let screenHeight: number;
    let containerWidth = 400;
    $: width =
        screenWidth >= 1024
            ? (containerWidth * 2) / 5
            : $currentStep == undefined || (screenWidth < 480 && $currentStep < 6)
            ? containerWidth * 1.25
            : containerWidth;
    let margin: Margin;
    $: margin = {
        top: width * 0.04,
        right: screenWidth >= 1024 ? 32 : 10,
        left: screenWidth >= 1024 ? 32 : 10 + (width > containerWidth ? containerWidth - width : 0),
        bottom: 0,
    };
    $: height = screenHeight * 0.8;
    $: rScale = scaleLinear()
        .domain([0, 1])
        .range([Math.max(1, width * 0.005), width * 0.03]);

    let tweenedX: Spring<number[]>;
    let tweenedY: Spring<number[]>;

    $: tweenedData = $dataManager.shots.map((shot, index) => ({
        x: tweenedX ? $tweenedX[index] : 0,
        y: tweenedY ? $tweenedY[index] : 0,
    }));

    let viewManager = new ViewManager();
    let currentStep = viewManager.currentStep;
    let currentStepTemp: number | undefined = undefined;
    let scrollY = 0;
    $: $currentStep =
        currentStepTemp === undefined && scrollY > screenHeight
            ? viewManager.steps.length - 1
            : currentStepTemp;
    let hoveredData = viewManager.hoveredData;
    setContext(viewKey, viewManager);

    function injectShotsConceded(data: DataManager) {
        if ($leagueShotsConceded == null) {
            console.log('Tried to inject leagueShotsConceded, but it was null!');
            return data;
        }
        data.opponents.setShotsConceded($leagueShotsConceded.teamShots);
        return data;
    }

    onMount(async () => {
        isMounted = true;

        const shotsAgainst = await data.streamed.shotsAgainst;
        const leagueShotsConcededObject = new LeagueShotsConceded(shotsAgainst);
        leagueShotsConceded.set(leagueShotsConcededObject);
        dataManager.update(injectShotsConceded);
    });
</script>

<svelte:window bind:innerWidth={screenWidth} bind:innerHeight={screenHeight} bind:scrollY />
<svelte:head>
    <title>{$dataManager.player.player_name} - Expected goals, visualised.</title>
</svelte:head>
<div
    class="!px-0 text-white-900 font-display"
    style="contain: paint;"
    bind:clientWidth={containerWidth}
>
    <Title />
    {#if isMounted}
        <VizContainer {width} {height} on:mouseleave={() => hoveredData.set(null)}>
            <svg {width} {height}>
                <g transform="translate({margin.left}, {margin.top})">
                    <VizManager {width} {height} {margin} {rScale} bind:tweenedX bind:tweenedY />
                    <XgCircles {rScale} data={tweenedData} />
                </g>
            </svg>
            {#if $hoveredData && $hoveredData.type == HoveredDataType.Shot}
                <Tooltip
                    limits={{
                        right: width - margin.right - margin.left,
                        bottom: height,
                        left: margin.left,
                        top: 0,
                    }}
                    x={$tweenedX[$hoveredData.index] + margin.left}
                    y={$tweenedY[$hoveredData.index] + margin.top}
                    offset={(rScale($hoveredData.data.xG) * 3) / 2}
                >
                    {#if $hoveredData != null}
                        <svelte:component this={$hoveredData.component} data={$hoveredData.data} />
                    {/if}
                </Tooltip>
            {/if}
        </VizContainer>
    {/if}
    <Scrolly bind:value={currentStepTemp}>
        <ContentManager />
    </Scrolly>
    <a href="/" class="mb-16 pl-16 font-medium text-md underline text-white-800"
        >Return to home page</a
    >
</div>
