import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8080';

const apiClient = {
    'get': async function(path, parameter) {
        return axios.get(path, parameter);
    }
};

export default apiClient;
