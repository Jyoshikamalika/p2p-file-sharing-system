from multi_peer_download import parallel_multi_peer_download

# Define peers
peers = [
    {"ip": "127.0.0.1", "port": 5001},
    {"ip": "127.0.0.1", "port": 5002},
    {"ip": "127.0.0.1", "port": 5003},
]

# Define chunk names
chunk_names = [
    f"myfile.txt_chunk{i}"
    for i in range(33)
]

# Paste your chunk hashes here
chunk_hashes = {

"myfile.txt_chunk0": "75857a45899985be4c4d941e90b6b396d6c92a4c7437aaf0bf102089fe21379d",
"myfile.txt_chunk1": "3faf5cca37f79214b589723c3a7aa4919d4249238fbb74c1938650aa2390e3cf",
"myfile.txt_chunk2": "0fb4989d1914dbc32c223cf9e473c4be5efb9f93dbce6b9875fba8aaddbf65a0",
"myfile.txt_chunk3": "4a7ce0b766a67a62a1a8ece2616cd35a820701afa894707ad21ec84c04bb7ee9",
"myfile.txt_chunk4": "d6b3f60d674543872f0270c654b290ba0c19253e3ad9efdecd8bf66454e54eee",
"myfile.txt_chunk5": "1106bf4ed4de42da196ef89390bda9a3afbfe5b4f809f75323554d2adb21d61d",
"myfile.txt_chunk6": "3b9c358f36f0a31b6ad3e14f309c7cf198ac9246e8316f9ce543d5b19ac02b80",
"myfile.txt_chunk7": "20d994eb8af2e1b29608231508a4de8463748800048eac0ccb0b4db10591c9ca",
"myfile.txt_chunk8": "d2f0f7477911d70de9f259e3ea67f07373d7f3d83c47a9b3dc944d71f5f77d93",
"myfile.txt_chunk9": "0d12579aab8ede2c5a5b1b2cc2cc166a8580906f6e78e96d16bb669e369eb7fa",
"myfile.txt_chunk10": "83e144c03b917e36e19f486bf473de5bdf3aedccb454b276e9c089ad36606c28",
"myfile.txt_chunk11": "4fc87f96d24ebe2a02b62a945afa10f1b7777da3fb12c1ba6fcff21d590b217c",
"myfile.txt_chunk12": "9603e1f11e5809bc2c4746afb4d2e49644a56b0f0a21879d7fd269991f82fe66",
"myfile.txt_chunk13": "0ade3c1fd271ef748b3a78f4bd342294aaecd91c079fdc35bfae14bb3f82c1af",
"myfile.txt_chunk14": "c794758a2f7be6a27a077403c89084bb78b7b4f2c72e323fd91dd8624f3929db",
"myfile.txt_chunk15": "f34da67695889d9257290f201b7f63f6c2dc6af2664756255e6b31436b50711c",
"myfile.txt_chunk16": "0f37b016b2b0c63b384229d1c514bc02a8033934d476c539b20db4e1067b107a",
"myfile.txt_chunk17": "6a4f9c5ca6db392304a58b371ea12f655c2584874108831f97d49b44c4b1536e",
"myfile.txt_chunk18": "443cdc5f92344aa06fe14002047badaed4b58071f29c5856044d9ffd2d5d2980",
"myfile.txt_chunk19": "a42d0af0b60e9208c40298f9882987dbbef0e76afcc655080005860984374f8e",
"myfile.txt_chunk20": "5886392ede6cfe3e2b9230134950e3e7237e46ad2821bffcd7e028cc9aa4b70c",
"myfile.txt_chunk21": "69f023cd3fa61ebed71fb8b24375aa016a9f3cfad316973ddb62ad1c1236b4f1",
"myfile.txt_chunk22": "1da290a0d91dc6571b98ed9042008de78101e2c1420e582d142b4b3385b7f59a",
"myfile.txt_chunk23": "0f37b016b2b0c63b384229d1c514bc02a8033934d476c539b20db4e1067b107a",
"myfile.txt_chunk24": "ef89e714f417cb6d25bdb4a2fe83802ebcaa08c5aea2bd8c7b2f546f5fb2e1b7",
"myfile.txt_chunk25": "c5b105ac2c28ad4f840f42af2251b90b6ecec6195ae919259227fa32b8e893cc",
"myfile.txt_chunk26": "c5353be4b3bc52507a5a87edcb9d35a3d55bf2da0635fbe440a429f1ceaf7cf8",
"myfile.txt_chunk27": "fe0663fd13cdb08743dca3d2d5d1168762556ea36f77d8ab6009306d12a6f351",
"myfile.txt_chunk28": "b5d1f9494822156cebe1fdeb15be7afa87db4a94be8dd7e709301ff384035333",
"myfile.txt_chunk29": "498d0f976ac0c31cbd140a275a96a67eaa3e61ec4e32f3b321622fba65047f4f",
"myfile.txt_chunk30": "3c307aa697b45603452ee8e373b9efda6a3140a9233d97bc89135fadadb744fc",
"myfile.txt_chunk31": "c896b47a822762b4691523d4c30d337564fde4e35c7b8cc97ba5b564061133c0",
"myfile.txt_chunk32": "3ef1e84b79d8b4df4dc588d05d5dd94428b61ed81f5534b4764d48412e8f2160",

}

# Start download
parallel_multi_peer_download(
    peers,
    chunk_names,
    chunk_hashes,
    "downloads/final_output.txt"
)