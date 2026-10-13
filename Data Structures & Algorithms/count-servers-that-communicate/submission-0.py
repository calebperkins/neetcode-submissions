def count_servers(grid):
    servers = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                servers.append((i, j))
    
    total_servers = len(servers)

    by_row = {}
    by_col = {}
    for item in servers:
        by_row.setdefault(item[0], []).append(item)
        by_col.setdefault(item[1], []).append(item)
    
    lone_servers = 0
    for row, servers_in_row in by_row.items():
        if len(servers_in_row) == 1:
            sr, sc = servers_in_row[0]
            if len(by_col[sc]) == 1:
                lone_servers += 1
    

    return total_servers - lone_servers


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        return count_servers(grid)