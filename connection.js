// import { SUPA_API_URL, SUPA_API_KEY } from "./config/supabase";
const SUPA_API_URL = "https://lejveivwlyrotymexzem.supabase.co/rest/v1/earthquakes";

const SUPA_API_KEY = "sb_publishable_Q94aJl0egnEtmAivKlEPCQ_-YRdp8hQ";
async function getEarthquakes({
    minTime,
    maxTime,
    minMagnitude,
    maxMagnitude,
    isEarthquake,
    limit = 70000,
} = {}) {
    const params = new URLSearchParams({
        select: "id,mag,time,type,title,x,y,z",
        order: "time.desc",
        limit: String(limit),
    });

    if (minTime) params.append("time", `gte.${minTime}`);
    if (maxTime) params.append("time", `lte.${maxTime}`);

    if (minMagnitude !== undefined && minMagnitude !== null && Number.isInteger(minMagnitude) && minMagnitude !== "") {
        params.append("mag", `gte.${minMagnitude}`);
    }

    if (maxMagnitude !== undefined && maxMagnitude !== null && Number.isInteger(maxMagnitude) && maxMagnitude !== "") {
        params.append("mag", `lte.${maxMagnitude}`);
    }

    if (isEarthquake === true) params.append("type","eq.earthquake");
    if (isEarthquake === false) params.append("type","neq.earthquake");

    const url = `${SUPA_API_URL}?${params.toString()}`;

    const res = await fetch(`${SUPA_API_URL}?${params}`, {
        headers: {
            apikey: SUPA_API_KEY,
            Authorization: `Bearer ${SUPA_API_KEY}`,
        },
    });

    if (!res.ok) {
        const error = await res.text();
        throw new Error(`ERROR: ${res.status} ${error}`);
    }

    return res.json();
}

getEarthquakes({
    minMagnitude: 0,
    maxMagnitude: 10,
    isEarthquake: false,
    limit: 70000,
}).then(console.log).catch(console.error);