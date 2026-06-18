async function getEarthquakes({
    minTime,
    maxTime,
    minMagnitude,
    maxMagnitude,
    isEarthquake.
    limit = 20,
}) {
    const params = new URLSearchParams({
        select: "id,mag,time,type,title,x,y,z",
        order: "time.desc",
        limit,
    });

    if (minTime) params.append("time", `gte.${minTime}`);
    if (maxTime) params.append("time", `gte.${maxTime}`);

    if (minMagnitude !=)

}