package com.frettafuria.gamedataapi.pubg;

import com.frettafuria.gamedataapi.battlefield2042.Battlefield2042Client;
import com.frettafuria.gamedataapi.battlefield2042.Battlefield2042PlatformType;
import com.frettafuria.gamedataapi.haloinfinite.HaloInfiniteClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/pubg")
public class PubgController {
    private PubgClient pubgClient;
    private Battlefield2042Client battlefield2042Client;
    private HaloInfiniteClient haloInfiniteClient;

    public PubgController(PubgClient pubgClient) { this.pubgClient = pubgClient; }

    @RequestMapping("/all")
    public String getAllResponses(){
        return String.format("PUBG:\n%s,\n%s,\n%s\nBattlefield 2042:\n%s\nHalo Infinite:\n%s",
                pubgClient.getMatchByMatchId("", PubgPlatformType.PSN),
                pubgClient.getPlayerByAccountId("", PubgPlatformType.XBOX),
                pubgClient.getTournamentByTournamentId("", PubgPlatformType.STEAM),
                battlefield2042Client.getPlayerByAccountId(0, Battlefield2042PlatformType.PS4),
                haloInfiniteClient.getMatchByMatchId("")
        );
    }

}
