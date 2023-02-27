<script lang='ts'>
    import { arc } from 'd3-shape';

    export let width: number;
    export let height: number;

    $: arcD = arc()
        .innerRadius(width * 10/74)
        .outerRadius(width * 10/74 + 2)
        .startAngle(Math.PI - Math.cos(6/10))
        .endAngle(Math.PI + Math.cos(6/10))

    $: arcCenter = arc()
        .innerRadius(width * 10/74)
        .outerRadius(width * 10/74 + 2)
        .startAngle(Math.PI * -1/2)
        .endAngle(Math.PI * 1/2)

    $: arcLeft = arc()
        .innerRadius(width * 1/74)
        .outerRadius(width * 1/74 + 2)
        .startAngle(Math.PI * 1/2)
        .endAngle(Math.PI)

    $: arcRight = arc()
        .innerRadius(width * 1/74)
        .outerRadius(width * 1/74 + 2)
        .startAngle(Math.PI)
        .endAngle(Math.PI * 3/2)

</script>

<!-- https://en.wikipedia.org/wiki/Football_pitch#/media/File:Soccer_pitch_dimensions.png -->
<!-- whole pitch -->
<rect
    width={width}
    height={height-2}
    fill="none"
    stroke="#999999"
    stroke-width=2
/>
<!-- 18yd box -->
<rect 
    x={width * ((74-44)/2)/74}
    width={width * 44 / 74}
    height={height * 18 / (115/2)}
    fill="none"
    stroke="#999999"
    stroke-width=2
/>
<!-- 6yd box -->
<rect
    x={width * ((74-20)/2)/74}
    width={width*20/74}
    height={height * 6 / (115/2)}
    fill="none"
    stroke="#999999"
    stroke-width=2
/>
<!-- goal -->
<rect
    x={width * ((74-8)/2)/74}
    y={-height * 2 / (115/2)}
    width={width*8/74}
    height={height * 2 / (115/2)}
    fill="none"
    stroke="#999999"
    stroke-width=2
/>
<!-- the d -->
<path 
    transform='translate({width/2},{height*10.8/(115/2)})'
    d={arcD()} 
    fill="#999999" 
/>
<!-- centre circle -->
<path 
    transform='translate({width/2},{height-2})'
    d={arcCenter()} 
    fill="#999999" 
/>
<!-- left corner -->
<path
    transform='translate(0,0})'
    d={arcLeft()}
    fill="#999999"
/>
<!-- right corner -->
<path
    transform='translate({width},0)'
    d={arcRight()}
    fill="#999999"
/>