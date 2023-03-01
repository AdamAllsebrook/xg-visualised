<script lang="ts">
    import type { Match, Shot } from '$client';
    import { scaleLinear} from 'd3-scale';
    import type { Spring } from 'svelte/motion';
	import { fade } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';
    
    export let width: number;
    export let height: number;
    export let matches: Match[];
    export let shots: Shot[];
    export let tweenedX: Spring<any>;
    export let tweenedY: Spring<any>;
    

    $: paddingY = height / (matches.length+1);
    $: matchesSorted = matches.sort((a, b) => Date.parse(a.date) - Date.parse(b.date));
    $: matchesMap = new Map(matchesSorted.map((match, i) => [match.id, i]));

    $: rScale = scaleLinear()
        .domain([0, 1])
        .range([Math.max(1, width*0.005), width*0.03])
    $: scale = (shot: Shot) => {
        return {
            x: Math.min(shot.minute, 90) * width / 90,
            y: (matchesMap.get(shot.match_id) || 0) * paddingY
        }
    }

    $: {scale; 
        tweenedX.set(shots.map(shot => scale(shot).x));
        tweenedY.set(shots.map(shot => scale(shot).y));
    }

</script>

<g  transition:fade="{{delay: 0, duration: 300, easing: cubicOut}}">
    {#each matchesSorted as match, i}
        <line
            x1=0
            x2={match.time_started * width / 90}
            y1={Math.round(i*paddingY)}
            y2={Math.round(i*paddingY)}
            stroke="#aaaaaa66"
            stroke-width=1
        />
        <rect
            x={match.time_started * width / 90}
            width={match.time * width / 90}
            y={Math.round(i*paddingY)-3}
            height=6
            rx=2
            stroke="black"
            stroke-width=1
            fill="#aaaaaa66"
        />
        <line
            x1={(match.time_started + match.time) * width / 90}
            x2={width}
            y1={Math.round(i*paddingY)}
            y2={Math.round(i*paddingY)}
            stroke="#aaaaaa66"
            stroke-width=1
        />
    {/each}
</g>