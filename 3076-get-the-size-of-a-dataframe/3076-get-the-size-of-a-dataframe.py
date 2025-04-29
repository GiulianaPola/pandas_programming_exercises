import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    num_cols=len(players.columns)
    num_rows=len(players.index)
    return [num_rows,num_cols]