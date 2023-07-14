#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h>
#include <pthread.h>

#define MAX_MESSAGE_LEN 1024

int sock;
pthread_t receive_thread;

void *receive_messages(void *arg) {
    char server_reply[MAX_MESSAGE_LEN];
    while (1) {
        // Receive a message from the server
        ssize_t received_bytes = recv(sock, server_reply, sizeof(server_reply), 0);
        if (received_bytes <= 0) {
            if (received_bytes == 0) {
                printf("Server disconnected\n");
            } else {
                perror("Receive failed");
            }
            break;
        }
        printf("\nReceived Message: %.*s\n", (int)received_bytes, server_reply);

        // Prompt the user to enter a message again
        printf("Enter message: ");
        fflush(stdout);  // Flush the output buffer before reading input
    }
    pthread_exit(NULL);
}

int main() {
    struct sockaddr_in server;
    char message[MAX_MESSAGE_LEN];

    // Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        perror("Failed to create socket");
        return 1;
    }

    server.sin_addr.s_addr = inet_addr("127.0.0.1");  // Replace with the actual IP address of the server
    server.sin_family = AF_INET;
    server.sin_port = htons(50000);  // Replace with the port used by the server

    // Connect to the remote server
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("Connection failed");
        return 1;
    }

    printf("Connected to the server\n");

    // Create a separate thread for receiving messages
    if (pthread_create(&receive_thread, NULL, receive_messages, NULL) != 0) {
        perror("Failed to create receive thread");
        return 1;
    }

    // Send messages
    while (1) {
        // Prompt the user to enter a message
        printf("Enter message: ");
        fflush(stdout);  // Flush the output buffer before reading input

        if (scanf("%s", message) != 1) {
            // Error occurred, exit the loop
            break;
        }

        // Send the message to the server
        ssize_t sent_bytes = send(sock, message, strlen(message), 0);
        if (sent_bytes <= 0) {
            if (errno == EPIPE) {
                printf("Server disconnected\n");
            } else {
                perror("Send failed");
            }
            break;
        }
    }

    // Wait for the receive thread to complete
    pthread_join(receive_thread, NULL);

    close(sock);

    return 0;
}
