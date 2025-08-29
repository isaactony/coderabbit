// Temporary fix for issue #123
function fetchData() {
    try {
        
        const data = externalService.getData();
        return data;
    } catch (error) {
        return null; 
    }
}
