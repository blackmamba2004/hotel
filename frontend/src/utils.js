function getAccessToken() {
    const match = document.cookie.match(/(^| )access_token=([^;]+)/);
    return match ? match[2] : null;
}

export default getAccessToken;