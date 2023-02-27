<script lang="ts">
	import type { Match, Shot } from '$client';

	export let width: number;
	export let height: number;
	export let matches: Match[];

	let matchOffset = new Map();
	$: {
		let sortedMatches = matches.sort((a, b) => Date.parse(a.date) - Date.parse(b.date));
		let offsets = sortedMatches.map((match, i) => sortedMatches.slice(0, i-1).map(x => x.time).reduce((x, y) => x + y, 0))
		sortedMatches.forEach((match, i) => {
			matchOffset.set(match.id, offsets[i] - match.time_started);
		})
	}

	let pathEl: SVGPathElement

	$: lineHeight = 80;
	// $: lineHeight = height / (38 / 2 + 1);
	$: maxLen = ((width + lineHeight) * 38) / 2;

	$: totalMinutes = matches.map((x) => x.time).reduce((x, y) => x + y, 0);
	$: length = (maxLen * totalMinutes) / 100 / 90;
	// $: length = maxLen;

	let y: number;
	const r = 10;
	let path: string[] = [];
	$: {
		path = ['M 0 0'];
		y = 0;
		for (let i = 0; i < length / (width + lineHeight) - 1; i++) {
			let x = i % 2 == 0 ? width : 0;
			let dir = x % 2 == 0 ? -1 : 1;
			let roundDir = x % 2 == 0 ? 0 : 1;
			path.push(`L ${x - r * dir} ${y}`);
			path.push(`A 10 10 0 0 ${roundDir} ${x} ${y + r}`);
			y += lineHeight;
			path.push(`L ${x} ${y - r}`);
			path.push(`A 10 10 0 0 ${roundDir} ${x - r * dir} ${y}`);
		}
		let lengthRemaining = ((length / (width + lineHeight)) % 1) * (width + lineHeight);
		let dir = Math.floor(length / (width + lineHeight)) % 2 ? -1 : 1;
		path.push(`l ${(dir * width * lengthRemaining) / (width + lineHeight)} 0`);
	}

	// https://gist.github.com/bycoffe/18441cddeb8fe147b719fab5e30b5d45
	function splitPath() {
		if (!pathEl) return [];
		let sampleInterval = 1;
		let cumu = 0;
		let pieceSizes = matches.map(x => length * x.time / totalMinutes);
		let pieces: string[] = [];

		pieceSizes.forEach((pieceSize, j) => {
			let segs = [];
			for (let i = 0; i <= pieceSize + sampleInterval; i += sampleInterval) {
				let pt = pathEl.getPointAtLength(i + cumu);
				segs.push([pt.x, pt.y]);
			}
			// let angle = (Math.atan2(segs[1][1] - segs[0][1], segs[1][0] - segs[0][0]) * 180) / Math.PI;
			// pieces.push({ id: j, segs: segs, angle: angle });
			let pathStr = `M ${segs[1][0]} ${segs[1][1]}`;
			segs.slice(2, -4).forEach(seg => pathStr += ` L ${seg[0]} ${seg[1]}`)
			pieces.push(pathStr);
			cumu += pieceSize;
		});

		return pieces;
	}

	let matchPaths: string[] = [];
	$: {pathEl; matchPaths = splitPath()}

	export const scale = (shot: Shot) => {
		let point = pathEl.getPointAtLength((matchOffset.get(shot.match_id) + shot.minute) / totalMinutes * length)
		return {x: point.x, y: point.y}
	}

</script>

<path d={path.join(' ')} bind:this={pathEl} display="none"/>

{#each matchPaths as p}
	<path d={p} fill="none" stroke="#000000" stroke-width="8"/>
{/each}
