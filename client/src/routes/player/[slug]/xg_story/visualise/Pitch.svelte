<script lang='ts'>
    import { arc } from 'd3-shape';
    import { scaleLinear } from 'd3-scale';
    import type { Shot } from '$client';
    import type { Tweened } from 'svelte/motion';
    import { tweened } from 'svelte/motion';
    import { cubicOut } from "svelte/easing";

    export let width: number;
    export let height: number;
    export let shots: Shot[];
    export let tweenedX: Tweened<any>;
    export let tweenedY: Tweened<any>;

    $: xScale = scaleLinear()
        .domain([0, 1])
        .range([width, 0])
    $: yScale = scaleLinear()
        .domain([0.5, 1])
        .range([height, 0])

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


    const tweenOptions = {
        delay: 0,
        duration: 750,
        easing: cubicOut,
    };

    $: {xScale, yScale
        if (!tweenedX && xScale && yScale) {
            tweenedX = tweened(
                shots.map(shot => xScale(shot.Y)),
                tweenOptions
            );
            tweenedY = tweened(
                shots.map(shot => yScale(shot.X)),
                tweenOptions
            );
        }
    }
    $: {xScale, yScale; 
        tweenedX.set(shots.map(shot => xScale(shot.Y)));
        tweenedY.set(shots.map(shot => yScale(shot.X)));
    }
    

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
