<script>
    export let height;
    export let xScale;
    export let margin;
    export let xTicks;
</script>

<g transform='translate({margin.left}, 0)'>
    {#each xTicks as [i, tick]}
        <text 
            x={xScale(i)} 
            y={height - margin.bottom}
            dy="6"
            dominant-baseline='hanging'
            text-anchor='middle'
            style='user-select: none'
        >
            {tick}
        </text>
        <line
            x1={xScale(i)}
            x2={xScale(i)}
            y1={height - margin.bottom - 2}
            y2={height - margin.bottom + 2}
            stroke='#cecece'
        />
    {/each}
</g>