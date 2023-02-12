<script>
    // export let height;
    export let width;
    export let yScale;
    export let margin;
  
    let yTicks = [0, 1, 2];
  </script>
  
  <g transform="translate(0 {margin.top})">
    {#each yTicks as tick, i}
        <text 
            x={0} 
            y={yScale(tick)}
            dy="-6"
            style='user-select: none'
            >{tick}.0 {i == yTicks.length-1 ? ' xG' : ''}
        </text>
        <line
            x1="0" 
            y1={yScale(tick)} 
            x2={width} 
            y2={yScale(tick)}
            stroke={i == 0 ? '#cecece' : '#cecece22'}
        />
    {/each}
  </g>