
![image](./kuvat/arkkitehtuuri.png)
```mermaid
sequenceDiagram
    actor Player
    participant GameLoop
    participant Level
    participant Head
    Player->>GameLoop: press "down" key
    GameLoop->>Level: turn_head("down")
    Level->>Head: queued_heading="down"
```
