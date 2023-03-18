<script lang='ts'>
    import { onMount } from 'svelte';
    import type { Spring } from 'svelte/motion';
    import { scaleLinear } from 'd3-scale';

    import { PlayerService } from '$client';
    import type { Player, Match, Season, Shot, SimpleShot, Fixture, Team } from '$client';

    import Scrolly from "$lib/Scrolly.svelte";
    import Tooltip from '$lib/Tooltip.svelte';
    import ShotTooltip from '$lib/ShotTooltip.svelte';
    import VizContainer from '$lib/VizContainer.svelte';
    import XgCircles from '$lib/XgCircles.svelte';
    import ContentManager from '$lib/ContentManager.svelte';
    import VizManager from '$lib/VizManager.svelte';
    import { colours } from '$lib/colours';
    import type { HoveredData } from '$lib/hoveredData';

    import Title from './Title.svelte';
    import { allShotsAgainst } from './stores.js';

    export let data: any;
    let player: Player = data.player;
    let matches: Match[] = data.matches;
    let shots: Shot[] = data.shots;
    let fixtures: Fixture[] = data.fixtures;
    let teams: Map<string, Team> = new Map(data.teams.map(x => [x.title, x]));

    let isMounted = false;
    let currentStep: number;

    let screenWidth: number;
    let screenHeight: number;
    let containerWidth = 400;
    $: width = screenWidth >= 1024 ? containerWidth * 2/5 : ((screenWidth < 480 && currentStep == 0 || currentStep == undefined) ? containerWidth * 1.25 : containerWidth);
    $: margin = { 
        top: width*0.04, 
        right: screenWidth >= 1024 ? 32 : 10, 
        left: screenWidth >= 1024 ? 32 : 10 + (width > containerWidth ? containerWidth - width : 0), 
        bottom: 0 
    };
    $: height = screenHeight * 0.8;
    $: rScale = scaleLinear()
        .domain([0, 1])
        .range([Math.max(1, width*0.005), width*0.03])

    let tweenedX: Spring<any>;
    let tweenedY: Spring<any>;

    $: tweenedData = shots.map((shot, index) => ({
        x: tweenedX ? $tweenedX[index] : 0,
        y: tweenedY ? $tweenedY[index] : 0
    }));

    let hoveredData: HoveredData | null;
    let svg;

    onMount(async () => {
        isMounted = true;
        if ($allShotsAgainst == null) {
            PlayerService.playerReadAllShots()
                .then(data => allShotsAgainst.set(data));
        }
    })

</script>

<svelte:window bind:innerWidth={screenWidth} bind:innerHeight={screenHeight} />
<div class="!px-0" style="contain: paint;" bind:clientWidth={containerWidth}>
    <Title {player} />
    {#if isMounted}
        <VizContainer {width} {height} on:mouseleave={() => hoveredData = null}>
            <svg {width} {height} bind:this={svg}>
                <g transform='translate({margin.left}, {margin.top})'>
                    <VizManager
                        {width}
                        {height}
                        {margin}
                        {currentStep}
                        {shots}
                        {matches}
                        bind:tweenedX
                        bind:tweenedY
                    />
                    <XgCircles
                        {shots}
                        {rScale}
                        data={tweenedData}
                        bind:hoveredData
                    />
                </g>
            </svg>
            {#if hoveredData}
                <Tooltip 
                    limits={{right: width-margin.right-margin.left, bottom: height, left: margin.left, top:0}}
                    x={$tweenedX[hoveredData.index] + margin.left}
                    y={$tweenedY[hoveredData.index] + margin.top}
                    offset={rScale(hoveredData.data.xG)*3/2}
                >
                    <!-- <ShotTooltip -->
                    <!--     shot={hoveredData.data} -->
                    <!-- /> -->
                    {#if hoveredData != null}
                        <svelte:component this={hoveredData.component} data={hoveredData.data}/>
                    {/if}
                </Tooltip>
            {/if}
        </VizContainer>
    {/if}
    <Scrolly bind:value={currentStep}>
        <ContentManager
            {currentStep}
            {player}
            {shots}
            {matches}
            {fixtures}
            {teams}
            {allShotsAgainst}
            bind:hoveredData
        />
    </Scrolly>
</div>
