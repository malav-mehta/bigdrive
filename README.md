<img src="https://i.ibb.co/PCFMF6P/logo.png" alt="BigDrive"/>

---

#### This project is in progress

## About

### A distributed file storage platform with client-hosted nodes

BigDrive is a cloud storage service inspired by Pied Piper's "Platform" from the TV show [Silicon Valley](https://en.wikipedia.org/wiki/Silicon_Valley). Instead of storing files on a centralized server, files are split into smaller chunks and distributed across a network of **client-hosted** storage nodes.

### Features

- **Secure:** All files are client-side encrypted before upload. Each node can only access its own chunks, and a node will only get one chunk per file. If someone managed to identify and acquire every chunk for a file, the chunks would need to be rearranged in the correct order, and then the file contents would need to be decrypted.
- **Big storage space:** Since storage space is contributed by users, users get storage space proportinal to how much they contribute. For every byte of space committed, a user receives 5 bytes of space on the network.
- **Globally accessible:** Files are accessible for download from any computer connected to the internet.
- **Easy-to-use:** Using the CLI app, a user can get started by signing up for an account, comitting local space and uploading their first file in less than a minute!
- **Reliable**: Every file chunk has redundancy to handle node failures or downtime. Each file chunk has two identical copies, and all three copies are stored on different nodes. If a node goes down, then a third copy is created automatically, so that there are always three copies for each chunk.

## API

The accompanying CLI offers an easy-to-use interface for users to manage their files and hosted nodes. Equivalently, files can be uploaded, deleted and downloaded from the public API. See the [Swagger file](./backend/api-gateway/api.yaml) for more details.

### Backend

The backend is built on GCP, with the below architecture.

<img src="https://i.ibb.co/qFfK26g/bigdrive.png" alt="BigDrive system architecture" />

## Running locally

Details for running BigDrive locally will be added once the project is completed.

## Tech stack

### CLI

- [Python](https://www.python.org/)
- [Click](https://click.palletsprojects.com/)

### Backend

- [Go](https://go.dev/)
- [API Gateway](https://cloud.google.com/api-gateway)
- [Cloud Storage](https://cloud.google.com/storage)
- [Cloud SQL](https://cloud.google.com/sql)
- [Cloud Run](https://cloud.google.com/run)
- [Pub/Sub](https://cloud.google.com/pubsub)
- [GKE](https://cloud.google.com/kubernetes-engine)
- [Firebase](https://firebase.google.com/)

## Contact

If you find any bugs or have any questions, feel free to email me: [malav.mehta@uwaterloo.ca](mailto:malav.mehta@uwaterloo.ca).
