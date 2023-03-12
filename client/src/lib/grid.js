export function grid(px, py, width) {
    let nRow = Math.floor(width / px) - 1;
    let a = 40, b = 0.05;
    return i => {
        return {
            x: px * (i % nRow + 1),
            y: py * (Math.floor(i / nRow) + 1)
            // x: width/2 + (a+b*i*px) * Math.cos(i*px),
            // y: width/2 + (a+b*i*px) * Math.sin(i*px)
        };
    }
}
