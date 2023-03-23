<script lang="ts">
    import { arc } from 'd3-shape';
    import { scaleLinear } from 'd3-scale';
    import type { Shot } from '$client';
    import type { Spring } from 'svelte/motion';
    import { spring } from 'svelte/motion';
    import { fade } from 'svelte/transition';
    import { cubicOut } from 'svelte/easing';
    import { key as dataKey, type DataManager } from './data/dataManager';
    import { getContext } from 'svelte';

    export let width: number;
    export let height: number;
    export let tweenedX: Spring<number[]>;
    export let tweenedY: Spring<number[]>;

    const dataManager: DataManager = getContext(dataKey);
    const shots: Shot[] = dataManager.shots;

    $: customHeight = (width * 0.5 * 115) / 74;

    $: xScale = scaleLinear().domain([0, 1]).range([width, 0]);
    $: yScale = scaleLinear().domain([0.5, 1]).range([customHeight, 0]);

    $: arcD = arc()
        .innerRadius((width * 10) / 74)
        .outerRadius((width * 10) / 74 + 2)
        .startAngle(Math.PI - Math.cos(6 / 10))
        .endAngle(Math.PI + Math.cos(6 / 10));

    $: arcCenter = arc()
        .innerRadius((width * 10) / 74)
        .outerRadius((width * 10) / 74 + 2)
        .startAngle((Math.PI * -1) / 2)
        .endAngle((Math.PI * 1) / 2);

    $: arcLeft = arc()
        .innerRadius((width * 1) / 74)
        .outerRadius((width * 1) / 74 + 2)
        .startAngle((Math.PI * 1) / 2)
        .endAngle(Math.PI);

    $: arcRight = arc()
        .innerRadius((width * 1) / 74)
        .outerRadius((width * 1) / 74 + 2)
        .startAngle(Math.PI)
        .endAngle((Math.PI * 3) / 2);

    const springConfig = {
        stiffness: 0.05,
        damping: 0.3,
        precision: 0.01,
    };
    $: {
        xScale, yScale;
        if (!tweenedX && xScale && yScale) {
            tweenedX = spring(
                shots.map((shot) => xScale(shot.Y)),
                springConfig,
            );
            tweenedY = spring(
                shots.map((shot) => yScale(shot.X) + (height - customHeight) / 2),
                springConfig,
            );
        }
    }
    $: {
        xScale, yScale;
        tweenedX.set(shots.map((shot) => xScale(shot.Y)));
        tweenedY.set(shots.map((shot) => yScale(shot.X) + (height - customHeight) / 2));
    }
</script>

<!-- https://en.wikipedia.org/wiki/Football_pitch#/media/File:Soccer_pitch_dimensions.png -->
<!-- whole pitch -->
<g
    transform="translate(0 {(height - customHeight) / 2})"
    transition:fade={{ delay: 0, duration: 300, easing: cubicOut }}
>
    <rect {width} height={customHeight - 2} fill="none" stroke="#999999" stroke-width="2" />
    <!-- 18yd box -->
    <rect
        x={(width * ((74 - 44) / 2)) / 74}
        width={(width * 44) / 74}
        height={(customHeight * 18) / (115 / 2)}
        fill="none"
        stroke="#999999"
        stroke-width="2"
    />
    <!-- 6yd box -->
    <rect
        x={(width * ((74 - 20) / 2)) / 74}
        width={(width * 20) / 74}
        height={(customHeight * 6) / (115 / 2)}
        fill="none"
        stroke="#999999"
        stroke-width="2"
    />
    <!-- goal -->
    <rect
        x={(width * ((74 - 8) / 2)) / 74}
        y={(-customHeight * 2) / (115 / 2)}
        width={(width * 8) / 74}
        height={(customHeight * 2) / (115 / 2)}
        fill="none"
        stroke="#999999"
        stroke-width="2"
    />
    <!-- the d -->
    <path
        transform="translate({width / 2},{(customHeight * 11.1) / (115 / 2)})"
        d={arcD()}
        fill="#999999"
    />
    <!-- centre circle -->
    <path transform="translate({width / 2},{customHeight - 2})" d={arcCenter()} fill="#999999" />
    <!-- left corner -->
    <path transform="translate(0,0})" d={arcLeft()} fill="#999999" />
    <!-- right corner -->
    <path transform="translate({width},0)" d={arcRight()} fill="#999999" />
</g>
