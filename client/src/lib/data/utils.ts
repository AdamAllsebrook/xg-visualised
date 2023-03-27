
export function sum(x: number, y: number) {
    return x + y;
}

export function bins(nums: number[], nBins: number, min: number, max: number): number[] {
    const size = max / nBins;
    let bins: number[] = [...Array(nBins).keys()]
        .map((bin) => bin * size)
        .map((bin) => nums.filter((num) => num >= bin && num < bin + size).length);
    return bins;
}
